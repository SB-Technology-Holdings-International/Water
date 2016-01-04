/*
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/
function loadJSON(path, success, error)
{
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function()
    {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                if (success) {
                    success(JSON.parse(xhr.responseText));
                }
            } else {
                if (error) {
                    error(xhr);
                }
            }
        }
    };
    xhr.open('GET', path, true);
    xhr.send();
}
(function(document) {
  'use strict';

  // Grab a reference to our auto-binding template
  // and give it some initial binding values
  // Learn more about auto-binding templates at http://goo.gl/Dx1u2g
  var app = document.querySelector('#app');

  app.loginOpen = true;


  app.valve0Header = 'Valve 1'
  app.valve1Header = 'Valve 2'
  app.valve2Header = 'Valve 3'
  app.valve3Header = 'Valve 4'
  app.valve0Header = localStorage.valve0Header
  app.valve1Header = localStorage.valve1Header
  app.valve2Header = localStorage.valve2Header
  app.valve3Header = localStorage.valve3Header

  var backend = document.getElementById('backend');
  CLIENT_ID = '';
  SCOPES = '';
  function signin(mode, authorizeCallback) {
    backend.auth.authorize({client_id: CLIENT_ID,
      scope: SCOPES, immediate: mode},
      authorizeCallback);
  }

  backend.addEventListener('google-api-load', function(event) {


    var request = backend.api.valve_info({
       device_id: 'test'
    });
    request.execute(function(resp) {
      app.valve0Header = resp.valves[0].name;
      localStorage.valve0Header = resp.valves[0].name;
      app.valve1Header = resp.valves[1].name;
      localStorage.valve1Header = resp.valves[1].name;
      app.valve2Header = resp.valves[2].name;
      localStorage.valve2Header = resp.valves[2].name;
      app.valve3Header = resp.valves[3].name;
      localStorage.valve3Header = resp.valves[3].name;
    });
  });

  app.usageTimeData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
      {
        label: 'My First dataset',
        fillColor: 'rgba(220,220,220,0.2)',
        strokeColor: 'rgba(220,220,220,1)',
        pointColor: 'rgba(220,220,220,1)',
        pointStrokeColor: '#fff',
        pointHighlightFill: '#fff',
        pointHighlightStroke: 'rgba(220,220,220,1)',
        data: [65, 59, 80, 81, 56, 55, 40]
      },
      {
        label: 'My Second dataset',
        fillColor: 'rgba(151,187,205,0.2)',
        strokeColor: 'rgba(151,187,205,1)',
        pointColor: 'rgba(151,187,205,1)',
        pointStrokeColor: '#fff',
        pointHighlightFill: '#fff',
        pointHighlightStroke: 'rgba(151,187,205,1)',
        data: [28, 48, 40, 19, 86, 27, 90]
      }
    ]
  };

  app.usageRelativeData = [
        {
          value: 300,
          color:'#F7464A',
          highlight: '#FF5A5E',
          label: 'Valve 1'
        },
        {
          value: 50,
          color: '#46BFBD',
          highlight: '#5AD3D1',
          label: 'Valve 2'
        },
        {
          value: 400,
          color: '#ADB45C',
          highlight: '#AFC870',
          label: 'Valve 3'
        },
        {
          value: 100,
          color: '#FDB45C',
          highlight: '#FFC870',
          label: 'Valve 4'
        }
      ];

      app.barData = {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
        {
          label: 'My First dataset',
          fillColor: 'rgba(220,220,220,0.2)',
          strokeColor: 'rgba(220,220,220,1)',
          pointColor: 'rgba(220,220,220,1)',
          pointStrokeColor: '#fff',
          pointHighlightFill: '#fff',
          pointHighlightStroke: 'rgba(220,220,220,1)',
          data: [65, 59, 80, 81, 56, 55, 40]
        },
        {
          label: 'My Second dataset',
          fillColor: 'rgba(151,187,205,0.2)',
          strokeColor: 'rgba(151,187,205,1)',
          pointColor: 'rgba(151,187,205,1)',
          pointStrokeColor: '#fff',
          pointHighlightFill: '#fff',
          pointHighlightStroke: 'rgba(151,187,205,1)',
          data: [28, 48, 40, 19, 86, 27, 90]
        }
      ]
      };

  app.newPlants = [];

  app.loginButtonPressed = function () {
    document.getElementById('loginButton').src = 'images/google_signin_pressed.svg';
    setTimeout( function () {
      document.getElementById('loginButton').src = 'images/google_signin.svg';
    }, 80 );
    // Login endpoints
  };

  // Sets app default base URL
  app.baseUrl = '/';
  if (window.location.port === '') {  // if production
    // Uncomment app.baseURL below and
    // set app.baseURL to '/your-pathname/' if running from folder in production
    // app.baseUrl = '/polymer-starter-kit/';
  }

  app.displayInstalledToast = function() {
    // Check to make sure caching is actually enabled—it won't be in the dev environment.
    if (!Polymer.dom(document).querySelector('platinum-sw-cache').disabled) {
      Polymer.dom(document).querySelector('#caching-complete').show();
    }
  };

  app.scheduleAdd = function() {
    document.querySelector('#schedule-add-done').show();
  };
  loadJSON('crop-names.json',
         function(data) { app.cropsList = data; },
         function(xhr) { console.error(xhr); }
  );

  app.cropInputChanged = function(e) {
    var input = (e.detail.value || '').trim().toLowerCase();
    if(typeof app.newPlants === 'undefined'){
       app.newPlants = [];
     }
    app.newPlants.forEach(function(z) {
        if (app.crops.indexOf(z.name) < 0) {
          var index = app.newPlants.indexOf(z);
          console.log('delete');
          app.splice('newPlants', index);
        }
    });
    if (input) {
      e.target.options = app.cropsList.filter(function(item) {
        return item.toLowerCase().indexOf(input) !== -1;
      });
      e.target.options.sort(function (a, b) {
        var aFirst = a.toLowerCase().indexOf(input) === 0;
        var bFirst = b.toLowerCase().indexOf(input) === 0;
        if (aFirst && !bFirst) {
          return -1;
        }
        if (!aFirst && bFirst) {
          return 1;
        }
        // a must be equal to b
        return 0;
      });
    }

    else {
      e.target.options = [];
    }
  };

  app.addCrop = function(e) {
    var input = (e.detail.value || '').trim();
    var plant = {};
    plant.name = input;
    plant.lower = input.toLowerCase();
    this.push('newPlants', plant);
  };

  // Listen for template bound event to know when bindings
  // have resolved and content has been stamped to the page
  app.addEventListener('dom-change', function() {
    console.log('Our app is ready to rock!');
  });

  // See https://github.com/Polymer/polymer/issues/1381
  window.addEventListener('WebComponentsReady', function() {
    // imports are loaded and elements have been registered
  });

  addEventListener('iron-select', function () {
      if (app.route === 'usage') {
        app.loadCharts = true;

      }
  });


  // Main area's paper-scroll-header-panel custom condensing transformation of
  // the appName in the middle-container and the bottom title in the bottom-container.
  // The appName is moved to top and shrunk on condensing. The bottom sub title
  // is shrunk to nothing on condensing.
  window.addEventListener('paper-header-transform', function(e) {
    var appName = Polymer.dom(document).querySelector('#mainToolbar .app-name');
    var middleContainer = Polymer.dom(document).querySelector('#mainToolbar .middle-container');
    var bottomContainer = Polymer.dom(document).querySelector('#mainToolbar .bottom-container');
    var detail = e.detail;
    var heightDiff = detail.height - detail.condensedHeight;
    var yRatio = Math.min(1, detail.y / heightDiff);
    // appName max size when condensed. The smaller the number the smaller the condensed size.
    var maxMiddleScale = 0.50;
    var auxHeight = heightDiff - detail.y;
    var auxScale = heightDiff / (1 - maxMiddleScale);
    var scaleMiddle = Math.max(maxMiddleScale, auxHeight / auxScale + maxMiddleScale);
    var scaleBottom = 1 - yRatio;

    // Move/translate middleContainer
    Polymer.Base.transform('translate3d(0,' + yRatio * 100 + '%,0)', middleContainer);

    // Scale bottomContainer and bottom sub title to nothing and back
    Polymer.Base.transform('scale(' + scaleBottom + ') translateZ(0)', bottomContainer);

    // Scale middleContainer appName
    Polymer.Base.transform('scale(' + scaleMiddle + ') translateZ(0)', appName);
  });

  // Scroll page to top and expand header
  app.scrollPageToTop = function() {
    app.$.headerPanelMain.scrollToTop(true);
  };

  app.closeDrawer = function() {
    app.$.paperDrawerPanel.closeDrawer();
  };

})(document);
