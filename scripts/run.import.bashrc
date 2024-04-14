run-3dgs() {
    local INPUT_NAME="$1"
    local OUTPUT_NAME="$2"

    date
    python train.py -s input/$INPUT_NAME -m output/$OUTPUT_NAME --eval && \
    python render.py -m output/$OUTPUT_NAME && \
    python metrics.py -m output/$OUTPUT_NAME
    date
}
