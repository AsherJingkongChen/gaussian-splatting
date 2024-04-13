run-3dgs() {
    local INPUT_NAME="$1"
    local OUTPUT_NAME="$2"

    date
    python train.py -s input/$INPUT_NAME -m output/$OUTPUT_NAME --eval && \
    python render.py -m output/$OUTPUT_NAME && \
    python metrics.py -m output/$OUTPUT_NAME
    date
}
run-report() {
    ./scripts/report.py > report/output.md
}
run-im2vd() {
    local IMAGE_GLOB="$1"
    local VIDEO_PATH="$2"

    ffmpeg \
        -y \
        -pattern_type glob \
        -i "$IMAGE_GLOB" \
        -framerate 60 -r 60 \
        -an -c:v libx265 -tag:v hvc1 \
        -crf 16 -preset medium \
        -pix_fmt yuv422p \
        -vf "scale=trunc(iw*3 / 2)*2:trunc(ih*3 / 2)*2" \
        "$VIDEO_PATH"
}

echo 'import {
    run-3dgs,
    run-report,
    run-im2vd,
} from "run.import.bashrc";'
