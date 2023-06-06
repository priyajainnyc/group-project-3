
    var labels = data.map(function (row) {
        return row.Month;
    });
    var values = data.map(function (row) {
        return row.Mining;
    });

    // Create the bar chart using Chart.js
    var ctx = document.getElementById('barChart').getContext('2d');
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                  
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    ;

