//Grab data
let industry_data = "/api/v1.0/quitrates_covid19_byindustry";
​
function init() {
  d3.json(industry_data).then(function(data) {
    console.log(data);
    let datasingle = data["Accommodation and food services"];
      let dataPlot = [{
        x: datasingle["Years"],
        y: datasingle["Rates"],
        type: 'bar'
      }]
      Plotly.newPlot("plot1", dataPlot);
    });
  }
// Function called by DOM changes
function refreshPlot() {
  let dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  let filter = dropdownMenu.property("value");
  // Call function to update the chart
  d3.json(industry_data).then(function(data) {
    let datasingle = data[filter];
    let dataPlot = [{
      x: datasingle["Years"],
      y: datasingle["Rates"],
      type: 'bar'
    }]
    Plotly.newPlot("plot1", dataPlot);
  });
}
// On change to the DOM, call getData()
d3.selectAll("#selDataset").on("change", refreshPlot);
init();