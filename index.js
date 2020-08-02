
const {app,  BrowserWindow } = require('electron')

 
// const {pyshell} =  require('python-shell');


// function  server() {
  
//   pyshell.run('server.py')
// }




function  boot() {
    win = new BrowserWindow()
    win.loadURL('http://127.0.0.1:8000/')
}


app.on('ready',  boot)


// const electron = require('electron');
// const app = electron.app;
// const BrowserWindow = electron.BrowserWindow;
// electron.crashReporter.start();

// var mainWindow = null;

// app.on('window-all-closed', function() {
//   //if (process.platform != 'darwin') {
//     app.quit();
//   //}
// });

// app.on('ready', function() {
//   // call python?
//   var subpy = require('child_process').spawn('python', ['./manage.py runserver']);
//   //var subpy = require('child_process').spawn('./dist/hello.exe');
//   var rq = require('request-promise');
//   var mainAddr = 'http://localhost:8000';

//   var openWindow = function(){
//     mainWindow = new BrowserWindow({width: 800, height: 600});
//     // mainWindow.loadURL('file://' + __dirname + '/index.html');
//     mainWindow.loadURL('http://localhost:8000');
//     mainWindow.webContents.openDevTools();
//     mainWindow.on('closed', function() {
//       mainWindow = null;
//       subpy.kill('SIGINT');
//     });
//   };

//   var startUp = function(){
//     rq(mainAddr)
//       .then(function(htmlString){
//         console.log('server started!');
//         openWindow();
//       })
//       .catch(function(err){
//         //console.log('waiting for the server start...');
//         startUp();
//       });
//   };

//   // fire!
//   startUp();
// });


