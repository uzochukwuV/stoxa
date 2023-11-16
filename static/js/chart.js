import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const aapl = [
    {date: '2007-04-23', close: 93.24},
    {date: '2007-04-24', close: 95.35},
    {date: '2007-04-25', close: 96.12},
    {date: '2007-04-26', close: 96.64},
    {date: '2007-04-27', close: 96.72},
    {date: '2007-04-30', close: 96.62},
    {date: '2007-05-01', close: 96.92},
    {date: '2007-05-02', close: 96.82},
    {date: '2007-05-03', close: 96.86},
    {date: '2007-05-04', close: 96.92},
    {date: '2007-05-07', close: 96.82},
    {date: '2007-05-08', close: 96.92},
    {date: '2007-05-09', close: 97.00},
    {date: '2007-05-10', close: 97.22},
]


console.log(aapl);

const chart =()=> {
    // Declare the chart dimensions and margins.
    const width = 208;
    const height = 140;
    const marginTop = 0;
    const marginRight = 0;
    const marginBottom = 0;
    const marginLeft = 0;
  
    // Declare the x (horizontal position) scale.
    const x = d3.scaleUtc(d3.extent(aapl, (d) => d.date), [50, width - marginRight]);
  
    // Declare the y (vertical position) scale.
    const y = d3.scaleLinear([0, 9000], [height - marginBottom, marginTop]);
  
    // Declare the line generator.
    const line = d3.line()
        .x(d => x(d.date))
        .y(d => y(d.close));
  
    // Create the SVG container.
    const svg = d3.create("svg")
        .attr("width", width)
        .attr("height", height)
        .attr("viewBox", [0, 0, width, height])
        .attr("style", "max-width: 100%; height: auto; height: intrinsic;font-size:8px;");
  
    // Add the x-axis.
    svg.append("g")
        .attr("transform", `translate(0,${height - marginBottom})`)
        .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0));
  
    // Add the y-axis, remove the domain line, add grid lines and a label.
    svg.append("g")
        .attr("transform", `translate(${50},0)`)
        .call(d3.axisLeft(y).ticks(height / 40))
        .call(g => g.select(".domain").remove())
        .call(g => g.selectAll(".tick line").clone()
            .attr("x2", width - 50 - marginRight)
            .attr("stroke-opacity", 0.04))
        .call(g => g.append("text")
            .attr("x", -50)
            .attr("y", 10)
            .attr("fill", "gray")
            .attr("text-anchor", "start")
            // .text("↑ Daily close ($)")
            );
  
    // Append a path for the line.
    svg.append("path")
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        // .attr("d", line(aapl));
  
    return svg.node();
  }

document.getElementById('chart').appendChild(chart())