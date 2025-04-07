//implement robots movement logs
function moveRobot(direction) {
    const logList = document.getElementById("log-list");
    const logEntry = document.createElement("li");
    logEntry.textContent = `Robot moved: ${direction}`;
    logList.appendChild(logEntry);
}

//implement random alerts (5-10 seconds)
function generateAlerts() {
    const alertList = document.getElementById("alert-list");
    const objects = ["Person Detected!", "Vehicle Detected!", "Motion Detected!"];

    setInterval(() => {
        if (Math.random() > 0.5) {
            const alertEntry = document.createElement("li");
            alertEntry.textContent = objects[Math.floor(Math.random() * objects.length)];
            alertList.appendChild(alertEntry);
        }
    }, Math.random() * 5000 + 5000);
}

//initialise map with API GPS data
function initMap() {
    const map = L.map("map").setView([53.8008, -1.5491], 15); // Leeds, UK (mock location)

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

    const marker = L.marker([53.8008, -1.5491]).addTo(map);
    marker.bindPopup("Robot's Current Location").openPopup();
}

//generate mock sensor data chart.js
function generateSensorChart() {
    const ctx = document.getElementById("sensorChart").getContext("2d");

    const sensorChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: [],
            datasets: [
                {
                    label: "Battery Level (%)",
                    borderColor: "blue",
                    data: [],
                },
                {
                    label: "Distance Sensor (m)",
                    borderColor: "red",
                    data: [],
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true },
            },
        },
    });

    //implement sensor data updates
    setInterval(() => {
        if (sensorChart.data.labels.length > 10) {
            sensorChart.data.labels.shift();
            sensorChart.data.datasets.forEach((dataset) => dataset.data.shift());
        }

        sensorChart.data.labels.push(new Date().toLocaleTimeString());
        sensorChart.data.datasets[0].data.push(Math.floor(Math.random() * 100)); //battery
        sensorChart.data.datasets[1].data.push((Math.random() * 2).toFixed(2)); //distance

        sensorChart.update();
    }, 2000);
}

//run simulations
generateAlerts();
initMap();
generateSensorChart();