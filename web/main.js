let paths = new Array();

function getPathToFile() {
  // Clean Old Paths
  paths = new Array();
  // Get new paths
  eel.dialogBox()(function (ret) {
    paths.push(ret);
  });
}

function save_js() {
  eel.save_py(paths);
  alert("Success");
}
