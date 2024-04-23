// server/index.js

const path = require("path");
const express = require("express");
const PORT = process.env.PORT || 3001;
const sample = require("./sample_data.json");

const app = express();
app.use(express.json()); // for parsing application/json
app.use(express.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded

const color_to_match = {
  L: 10.60330918067893,
  A: 13.480786348810863,
  B: -25.02938394226518,
};

const distance = (color1, color2) => {
  return Math.sqrt(
    (color1.L - color2.L) ** 2 +
      (color1.A - color2.A) ** 2 +
      (color1.B - color2.B) ** 2
  );
};

const find_shortest_distance = (color, data) => {
  var shortest_distance;
  var product;
  for (let i = 0; i < data.length; i++) {
    if (
      distance(color, data[i].color) < shortest_distance ||
      shortest_distance === undefined
    ) {
      shortest_distance = distance(color, data[i].color);
      product = data[i];
    }
  }
  //console.log(shortest_distance)
  return product;
};



app.get("/", (req, res) =>{
  res.send("hey")
})

// Have Node serve the files for our built React app
//app.use(express.static(path.resolve(__dirname, "../client/build")));

app.post("/api", (req, res) => {
  console.log(req.body);
  console.log(distance(color_to_match, req.body.color));
  res.send("Hello");
})

app.get("/api", (req, res) => {
  res.send("Hello");
});
  /*
  var result = find_shortest_distance(req.body.color, sample);
 
  res.status(200).json({
    image: result.swatch,
    name: result.name,
    hex: result.hex,
    brand: result.brand,
  });
});
*/

// All other GET requests not handled before will return our React app
app.get("*", (req, res) => {
  res.send(("This is not where you should be"));
});

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});

module.exports = app