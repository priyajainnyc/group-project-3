// Grab data
let apiLine = "/api/v1.0/ratesdata";
function init() {
  d3.json(apiLine).then(function(data) {
    console.log(data);
    let datasingle = data["Hire Rate"];
      let dataPlot = [{
        x: datasingle["Years"],//Object.keys(data),
        y: datasingle["Rates"],//Object.values(data),
        type: 'line'
      }]
      Plotly.newPlot("plot", dataPlot);
    });
  }
// Function called by DOM changes
function refreshPlot() {
  let dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  // Call function to update the chart
  d3.json(apiLine).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],//Object.keys(data),
      y: datasingle["Rates"],//Object.values(data),
      type: 'line'
    }]
    Plotly.newPlot("plot", dataPlot);
  });
}
// On change to the DOM, call getData()
d3.selectAll("#selDataset").on("change", refreshPlot);
init();
