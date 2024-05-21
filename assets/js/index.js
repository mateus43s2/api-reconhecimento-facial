const video = document.getElementById('video')

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('./assets/lib/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('./assets/lib/models'),
]).then(startVideo)


video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)

    if (detections[0].expressions) {
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify({
        "local_name": "test",
        "created_at": "2021-07-09T20:48:09.859650Z",
        "angry": detections[0].expressions.angry,
        "disgusted": detections[0].expressions.disgusted,
        "fearful": detections[0].expressions.fearful,
        "happy": detections[0].expressions.happy,
        "neutral": detections[0].expressions.neutral,
        "sad": detections[0].expressions.sad,
        "surprised": detections[0].expressions.surprised
      });

      var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };

      fetch("http://127.0.0.1:8000/facial/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
    }

  }, 1000)
})
