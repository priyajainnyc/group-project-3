// Create an array of each country's numbers
let Construction = Object.values(data.Construction);
let RetailTrade = Object.values(data.RetailTrade);
let Transportation_Warehousing_Utilities= Object.values(data.Transportation_Warehousing_Utilities);
let Arts_Entertainment_Recreation= Object.values(data.Arts_Entertainment_Recreation);
let Accommodation_FoodServices= Object.values(data.Accommodation_FoodServices);

// Create an array of category labels
let labels = Object.keys(data.Construction);
// console.log(Construction);

//bubble chart
function init() {
    var dataPlot = [{
        values: Construction,
        labels: labels,
        // text: labels,
    //     mode: "markers",
    //   marker: {
    //     color: labels,
    //     size: values
    //   }
    }];

    var layout = {
        // showlegend: false,
        height: 500,
        width: 900
    };
  
    Plotly.newPlot("bubble", dataPlot, layout);
};


function updatePlot() {
    let dropdownMenu = d3.select("#selDataset");
    let datasetName = dropdownMenu.property("value");

    let x = [];
    let y = labels;

    if (datasetName == 'Construction') {
    x = Construction;
    }
    else if (datasetName == 'RetailTrade') {
      x = RetailTrade;
    }
    else if (datasetName == 'Transportation_Warehousing_Utilities') {
      x = Transportation_Warehousing_Utilities;
     }
     else if (datasetName == 'Arts_Entertainment_Recreation') {
    x = Arts_Entertainment_Recreation;
     }
    else if (datasetName == 'Accommodation_FoodServices') {
      x = Accommodation_FoodServices;
    }

    Plotly.restyle("bubble", "values", [x]);
}

let myDropDown = d3.select("#selDataset")
myDropDown.on("click", updatePlot);

init();

console.log(x)



// // On change to the DOM, call getData()
// d3.selectAll("#selDataset").on("change", getData);

// // Function called by DOM changes
// function getData() {
//   let dropdownMenu = d3.select("#selDataset");
//   // Assign the value of the dropdown menu option to a letiable
//   let dataset = dropdownMenu.property("value");
//   // Initialize an empty array for the country's data
//   let data = [];

//   if (dataset == 'Construction') {
//       data = Construction;
//   }
//   else if (dataset == 'RetailTrade') {
//       data = RetailTrade;
//   }
//   else if (dataset == 'Transportation, Warehousing, Utilities') {
//       data = Transportation, Warehousing, Utilities;
//   }
//   else if (dataset == 'Arts, Entertainment, Recreation') {
//     data = Arts, Entertainment, Recreation;
//   }
//   else if (dataset == 'Accommodation, FoodServices') {
//       data = Accommodation, FoodServices;
//   }
// // Call function to update the chart
//   updatePlotly(data);
// }

// // Update the restyled plot's values
// function updatePlotly(newdata) {
//   Plotly.restyle("bubble", "values", [newdata]);
// }

init();







// function showbubblechart(sampleid) {
//     d3.json(url).then(function (data) {
//         let samples = data.samples
//         let samplearray = samples.filter(sample => sample.id == sampleid)
//         let sample = samplearray[0]
//         let values = sample.sample_values
//         let ids = sample.otu_ids
//         let labels = sample.otu_labels
 

// let trace1 = {
//     x: ids,
//     y: values,
//     text: labels,
//     mode: "markers",
//   marker: {
//     color: ids,
//     size: values
//   }
// };
    
// let dataPlot1 = [trace1];

// // Apply a title to the layout
// let layout = {
//     showlegend: false,
//   height: 500,
//   width: 900
// }

// Plotly.newPlot("bubble", dataPlot1, layout);
// });

// };











// // Initializes the page with a default plot
// function init() {
//     let dropdown = d3.select("#selDataset")
//     d3.json(url).then(function (data) {
//         let samplenames = data.names
//         for (let i = 0; i < samplenames.length; i++) {
//             dropdown.append("option").text(samplenames[i]).property("value", samplenames[i])
//         }
//         console.log(data);
//         let firstsample = samplenames[0]
//         showbarchart(firstsample)
//         showbubblechart(firstsample)
//         showmetadata(firstsample)
//     });
// };

// init();

// function showmetadata(sampleid) {
//     d3.json(url).then(function (data) {
//         let metadata = data.metadata;
//         let metadataarray = metadata.filter(sample => sample.id == sampleid);
//         let result = metadataarray[0];
//         console.log(result);
//         let some_var = d3.select("#sample-metadata");
//         some_var.html("");
//         for (category in result){
//             some_var.append("h5").text(`${category}: ${result[category]}`);
//         };
//     })
    
// }



// function optionChanged(newsample) {
//     showbarchart(newsample)
//     showbubblechart(newsample)
//     showmetadata(newsample)
// }

// function showbarchart(sampleid) {
//     d3.json(url).then(function (data) {
//         let samples = data.samples
//         let samplearray = samples.filter(sample => sample.id == sampleid)
//         let sample = samplearray[0]
//         let values = sample.sample_values
//         let ids = sample.otu_ids
//         let labels = sample.otu_labels
        
//         // console.log(sample)
//         // console.log(ids)
//         // console.log(labels)
//         // console.log(values)

// // bar chart
//         let trace = {
//         x: values.slice(0,10).reverse(),
//         y: ids.slice(0,10).map(id => `OTU ${id}`).reverse(),
//         text: labels.slice(0,10).reverse(),
//         type: "bar",
//         orientation: "h"
//         };


// // Apply a title to the layout
//         let layout = {
//         //  title: "Top 10 OTUs",
//          margin: {
//          l: 100,
//          r: 100,
//          t: 100,
//          b: 100
//          }
// };

// // Data trace array
// let dataPlot = [trace];

// //Plot
// Plotly.newPlot("bar", dataPlot, layout);
//     })

// }

// //bubble chart
// function showbubblechart(sampleid) {
//     d3.json(url).then(function (data) {
//         let samples = data.samples
//         let samplearray = samples.filter(sample => sample.id == sampleid)
//         let sample = samplearray[0]
//         let values = sample.sample_values
//         let ids = sample.otu_ids
//         let labels = sample.otu_labels
 

// let trace1 = {
//     x: ids,
//     y: values,
//     text: labels,
//     mode: "markers",
//   marker: {
//     color: ids,
//     size: values
//   }
// };
    
// let dataPlot1 = [trace1];

// // Apply a title to the layout
// let layout = {
//     showlegend: false,
//   height: 500,
//   width: 900
// }

// Plotly.newPlot("bubble", dataPlot1, layout);
// });

// };


