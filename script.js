function changeVideo() {
    var videoPlayer = document.getElementById("videoPlayer");
    var videoSelect = document.getElementById("videoSelect");
    var selectedVideo = videoSelect.value;
    
    // Set the video source
    videoPlayer.src = selectedVideo;
    videoPlayer.load();
}

function changeGraph() {
    var graphSelect = document.getElementById("graphSelect");
    var selectedGraph = graphSelect.value;
    
    // Render the selected graph
    renderGraph(selectedGraph);
}

function renderGraph(graphType) {
    // Code to render the selected graph based on the graphType value
    // You'll need to use a library like Chart.js or D3.js to create the graph
}

// Call the initial functions if needed
changeVideo();
changeGraph();
