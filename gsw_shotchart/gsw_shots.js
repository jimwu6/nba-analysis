d3.csv("gsw.csv", function(data)
{
    console.log(data);
    d3.select("svg")
    .selectAll("g")
        .data(data)
        .enter()
        .append("g")
            .attr("class", "shot")
                .attr("transform", function(d){
                    return "translate(" + 10 * d.converted_y + "," + 10 * d.converted_x +")";
                })
    shots.append("circle")
        .attr("r", 5)
        .attr("fill", function(d){
        if(d.result=="made"){
            return "green";
        }
        else{
            return "red";
        }
        })
})
