//Grab data
let industry_data2 = "/api/v1.0/sectorquits";
function init() {
  d3.json(industry_data2).then(function(data) {
    console.log(data);
    let datasingle = data["Manufacturing"];
      let dataPlot = [{
        x: datasingle["Years"],
        y: datasingle["Rates"],
        type: 'bar'
      }]
      Plotly.newPlot("plot2", dataPlot);
    });
  }
// Function called by DOM changes
function refreshPlot() {
  let dropdownMenu = d3.select("#selDataset2");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  // Call function to update the chart
  d3.json(industry_data2).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],
      y: datasingle["Rates"],
      type: 'bar'
    }]
    Plotly.newPlot("plot2", dataPlot);
  });
}
// On change to the DOM, call getData()
d3.selectAll("#selDataset2").on("change", refreshPlot);
init();