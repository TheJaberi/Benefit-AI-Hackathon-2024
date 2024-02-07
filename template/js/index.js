d3.csv("../data/prophet_forecast.csv").then(function(data) {
    // Log the data to the console to see what it looks like
    console.log(data);

    // Create a scale for the x and y axes
    var xScale = d3.scaleLinear().domain([0, d3.max(data, function(d) { return d.x; })]).range([0, 500]);
    var yScale = d3.scaleLinear().domain([0, d3.max(data, function(d) { return d.y; })]).range([500, 0]);

    // Create the x and y axes
    var xAxis = d3.axisBottom().scale(xScale);
    var yAxis = d3.axisLeft().scale(yScale);

    // Append the axes to the SVG
    d3.select("svg").append("g").call(xAxis);
    d3.select("svg").append("g").call(yAxis);

    // Create the line
    var line = d3.line()
        .x(function(d) { return xScale(d.x); })
        .y(function(d) { return yScale(d.y); });

    // Append the line to the SVG
    d3.select("svg").append("path")
        .datum(data)
        .attr("d", line);
});