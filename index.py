
html_code = '''
<!DOCTYPE html>
<html>
<head>
  <style>
        body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-image: url("Background].jpg"); /* Replace "background-image.jpg" with your own image path */
      background-size: cover;
      background-color: rgba(195, 194, 194, 0.9);
    }

    h1 {
      text-align: center;
    }

    .container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      margin-top: 50px;
    }

    .photo {
      position: relative;
      margin: 10px;
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      border-radius: 7px; /* Adjust the value to make the borders more or less round */
      overflow: hidden; /* Clip the content within the rounded borders */
    }

    .dropdown {
      position: absolute;
      top: 10px;
      left: 10px;
      z-index: 1;
      background-color: #a6211c;
      padding: 5px;
      border-radius: 0;
    }

    .dropdown select {
      border: none;
      color: #ffffff;
      font-size: 16px;
      background-color: #a6211c;
    }

    .photo img {
      height: calc(100% - 6px);
      width: calc(100% - 6px);
      object-fit: cover;
    }

    .video-container {
      position: relative;
      width: 100%;
      height: 100%;
    }
    .video-container .bordered-video,
    .video-container .bordered-video2 {
      border: 4px solid #a6211c;
      box-sizing: content-box;
      height: 100%;
      width: 100%;
      object-fit: cover;
      position:absolute
    }



    .middle-image {
      flex: 1;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .middle-image img {
      height: 100px;
      max-width: 100%;
    }
    /* CSS for the pop-up */
    .popup {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(156, 153, 153, 0.9); /* Semi-transparent background */
      display: flex;
      justify-content: center;
      align-items: center;
      z-index: 9999;
    }

    .popup-content {
      position: relative;
      max-width: 80%;
      max-height: 80%;
      overflow: hidden;
    }

    .popup-image {
      display: block;
      max-width: 40%;
      max-height: 40%;
      margin: 0 auto;
    }

    
    .bordered-canvas {
      border: 2px solid #a6211c;
      box-sizing: border-box;
      height: 50%;
      width: 100%;
      padding: 1px;
    }

    .bordered-canvas2 {
      border: 2px solid #a6211c;
      box-sizing: border-box;
      height: 50%;
      width: 100%;
      padding: 1px;
    }

    .close-button {
      position: absolute;
      bottom: 3px;
      left: 50%;
      transform: translateX(-50%);
      background-color: #f50404;
      color: #fff;
      padding: 7px 10px;
      border: none;
      border-radius: 3px;
      cursor: pointer;
    }

    .close-button:hover {
      background-color: #c40000;
      border: none;
      color: #ffffff;
      font-size: 16px;
      background-color: #a6211c;
    }

    #graphCanvas {
      display: none;
      max-width: 100%;
      height: auto;
    }

    #graphCanvas2 {
      display: none;
      max-width: 100%;
      height: auto;
    }
  </style>
  
</head>
<body>
  <div class="container">
    <div class="middle-image">
      <img src="LOgo.png" alt="Middle Image">
    </div>
  </div>

  <div class="container">
    <div class="photo">
      <div class="dropdown">
        <select onchange="toggleWaitingTimeImage(this)">
          <option value="option1">Route 1</option>
          <option value="option2">Route 2</option>
          <option value="option3">Route 3</option>
          <option value="option3">Route 4</option>
        </select>
      </div>
      <div class="video-container">
        <video autoplay loop class="bordered-video2" Id="myVideo2" src="assets/final.mp4" alt="Video 2" onclick="openPopup('Blabla.png')" controls></video>
        <video autoplay loop class="bordered-video" Id="myVideo" src="assets/final2.mp4" alt="Video 1" onclick="openPopup('Blabla.png')" controls>
      </div>
    </div>
    <div class="photo">
      <div class="dropdown">
        <select id="dataSelect">
          <option value="option1">Nombre de véhicule</option>
          <option value="option3">Temps d'attente moyen</option>
          <option value="option2">Émissions CO2</option>
          <option value="option3">Consommation de carburant</option>
        </select>
      </div>
      <canvas id="graphCanvas" class="bordered-canvas"></canvas>
      <canvas id="graphCanvas" class="bordered-canvas2"></canvas>
    </div>
      
  </div>

  <div class="popup" id="popup" onclick="closePopup()">
    <div class="popup-content">
      <img class="popup-image" src="Hilal.jpg" alt="Popup Image">
      <button class="close-button">For Lives</button>
    </div>
  </div>


    
  
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script>

    var graphData = [0, 2624.722222, 4288.991037, 6350.491414, 6556.09518, 8029.371725, 11708.21793, 14070.62144, 4315.704623,
    8586.050704, 7335.164894, 13634.76945, 2595.42689, 2567.401196, 2615.075426, 2622.75146, 2624.722222,
    2624.722222, 5218.861523, 5243.651681, 5246.911249, 7874.087357, 9157.652525, 10935.24894, 13451.97311,
    11187.90492, 18314.91563, 11968.20701, 5249.444444, 5249.444444, 5249.444444, 5249.444444, 7836.119511,
    7870.524729, 7873.909631, 7874.137688, 10498.88889, 11728.72976, 11691.9221, 14116.80956, 14410.258,
    22110.25545, 7874.166667, 13666.32975, 7874.166667, 7874.166667, 7874.166667, 10416.04995, 10488.09127,
    10492.5132, 10492.79731, 13123.4755, 15504.8102, 14668.03908, 17244.81935, 18745.67937, 24254.24256,
    13957.62341, 14214.52332, 14651.08671, 17620.97103, 19337.9815, 24250.54183, 17237.61491, 20501.95238,
    20615.96427, 21278.75659, 15714.31325, 15727.96216, 15735.90175, 18305.88257, 18365.41987, 18371.51676,
    18372.19827, 18373.00252, 18373.0383, 18373.05556, 18373.05556, 18373.05556, 18373.05556, 18373.05556,
    20997.77778, 22608.84169, 22742.77052, 23578.59984, 27413.38614, 20997.77778, 21705.56361, 21594.62922,
    24148.13067, 24727.14105, 25057.55354, 20997.77778, 20997.77778, 20997.77778, 23614.45098, 23622.47,
    23622.48549, 23622.5, 23622.5, 23622.5, 23622.5, 23622.5, 23622.5, 23622];
    
    var graphData2 = [0,1, 5249.444444, 5249.444444, 5249.444444, 5249.444444, 7836.119511,
    7870.524729, 7873.909631, 7874.137688, 10498.88889, 11728.72976, 11691.9221, 14116.80956, 14410.258,
    22110.25545, 7874.166667, 13666.32975, 7874.166667, 7874.166667, 7874.166667, 10416.04995, 10488.09127,
    10492.5132, 10492.79731, 13123 ,722222, 4288.991037, 6350.491414, 6556.09518, 8029.371725, 11708.21793, 14070.62144, 4315.704623,
    8586.050704, 7335.164894, 13634.76945, 2595.42689, 2567.401196, 2615.075426, 2622.75146, 2624.722222,
    2624.722222, 5218.861523, 5243.651681, 5246.911249, 7874.087357, 9157.652525, 10935.24894, 13451.97311,
    11187.90492, 18314.91563, 11968.2070556, 18373.05556, 18373.05556, 18373.05556, 18373.05556,
    20997.77778, 22608.84169, 22742.77052, 23578.59984, 27413.38614, 20997.77778, 21705.56361, 21594.62922,
    24148.13067, 24727.14105, 25057.55354, 20997.77778, 20997.77778, 20997.77778, 23614.45098, 23622.47,
    23622.48549, 23622.5, 23622.5, 23622.5, 23622.5, 23622.5, 23622.5, 23622];

    function renderGraph(data) {
      var labels = data.map(function(_, index) {
        return index + 1;
      });

      var ctx = document.getElementById('graphCanvas').getContext('2d');
      var chartData = {
        labels: labels,
        datasets: [{
          label: 'Graph Data',
          data: data,
          backgroundColor: 'rgba(166, 33, 28, 0.5)',
          borderColor: 'rgba(166, 33, 28, 1)',
          borderWidth: 2
        }]
      };
      var options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };
      new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: options
      });
    }

    // render graph pour data 2
    function renderGraph2(data) {
      var labels = data.map(function(_, index) {
        return index + 1;
      });

      var ctx = document.getElementsByClassName('bordered-canvas2').getContext('2d');
      var chartData = {
        labels: labels,
        datasets: [{
          label: 'Graph',
          data: data,
          backgroundColor: 'rgba(166, 33, 28, 0.5)',
          borderColor: 'rgba(166, 33, 28, 1)',
          borderWidth: 2
        }]
      };
      var options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      };
      new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: options
      });
    }

    function updateGraphData(currentData) {
      graphData.push(currentData); // Ajoutez la nouvelle donnée à la fin de graphData

      // Mettez à jour le graphique avec les nouvelles données
      var chart = Chart.instances[0];
      chart.data.labels.push(chart.data.labels.length + 1);
      chart.data.datasets[0].data.push(currentData);

      if (chart.data.labels.length > 50) {
        // Supprimez les données excédentes si elles dépassent 50 éléments
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
      }

      chart.update();
    }

    function initializeGraph() {
      // Obtenez les 50 premières valeurs de graphData
      var initialData = graphData.slice(0, 50);

      renderGraph(initialData);

      // Simulez les mises à jour de données périodiques
      setInterval(function() {
        var randomValue = Math.random() * 10000;
        updateGraphData(randomValue);
      }, 2000);
    }

    initializeGraph();

    // pour le deuxième graphe
    function updateGraphData(currentData) {
      graphData2.push(currentData); // Ajoutez la nouvelle donnée à la fin de graphData

      // Mettez à jour le graphique avec les nouvelles données
      var chart = Chart.instances[0];
      chart.data.labels.push(chart.data.labels.length + 1);
      chart.data.datasets[0].data.push(currentData);

      if (chart.data.labels.length > 50) {
        // Supprimez les données excédentes si elles dépassent 50 éléments
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
      }

      chart.update();
    }

    function initializeGraph2() {
      // Obtenez les 50 premières valeurs de graphData
      var initialData = graphData2.slice(0, 50);

      renderGraph2(initialData);

      // Simulez les mises à jour de données périodiques
      setInterval(function() {
        var randomValue = Math.random() * 10000;
        updateGraphData2(randomValue);
      }, 2000);
    }

    initializeGraph2();

    function toggleWaitingTimeImage(selectElement) {

      var videoElement = document.getElementById('myVideo');
      var videoElement2 = document.getElementById('myVideo2');
      var graphCanvas = document.getElementById('graphCanvas');
      var graphCanvas2 = document.querySelector('bordered-canvas2');
      var isVisible = selectElement.value === 'option1';
      var isVisible2 = selectElement.value === 'option2';
      
      if (isVisible) {
        graphCanvas.style.display = 'block';
        videoElement.style.display = 'block';
        videoElement2.style.display = 'none';
        videoElement.play(); // Démarrer la lecture de la vidéo
        renderGraph(graphData);

      } else if (isVisible2) {
        graphCanvas.style.display = 'block';
        videoElement.style.display = 'none';
        videoElement2.style.display = 'block';
        videoElement2.play();
        renderGraph2(graphData2);

      } else {
        graphCanvas.style.display = 'none';
        videoElement.pause();
        videoElement2.pause(); // Mettre en pause la vidéo
      }

    }
  

    function openPopup(imageSrc) {
      var popupImage = document.querySelector('.popup-image');
      popupImage.src = imageSrc;
      document.getElementById("popup").style.display = "flex";
    }

    function closePopup() {
      document.getElementById("popup").style.display = "none";
    }
    
  </script>
</body>
</html>
'''

with open('Popup.html', 'w') as file:
    file.write(html_code)

