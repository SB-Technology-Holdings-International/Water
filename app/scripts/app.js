/*
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/
/* jshint -W106 */
// jscs:disable requireCamelCaseOrUpperCaseIdentifiers

function loadJSON(path, success, error) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
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
  app.geoIdle = true;

  app.loginOpen = true;
  app.apiRoot = '//' + window.location.host + '/_ah/api';
  app.lat = 37.0;
  app.lng = -120.0;
  app.mapZoom = 6;
  app.valve0 = {};

  var i = 0;
  if (!localStorage.valves) {
    app.valves = {};
    for (i = 0; i < 4; i++) {
      app.valves[i] = {};
      app.valves[i].header = 'Valve ' + String(i + 1);
      app.valves[i].startIndex = 1;
      app.valves[i].hours = 0;
      app.valves[i].minutes = 0;
    }
    localStorage.valves = JSON.stringify(app.valves);
  } else {
    app.valves = JSON.parse(localStorage.valves);
  }

  var backend = document.getElementById('backend');
  var CLIENT_ID = '651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com';
  var SCOPES = ['email', 'profile'];

  function signin(mode, authorizeCallback) {
    backend.auth.authorize({client_id: CLIENT_ID,
      scope: SCOPES, immediate: mode},
      authorizeCallback);
  }

  function userAuthed() {
    if (backend.auth.getToken()) {
      // User is signed in, call Endpoint
      app.waterApi = backend.api;
      var request = app.waterApi.check_user({
      });
      request.execute(function(resp) {
        if (resp.device_id) { // Ok get data
          app.device_id = resp.device_id;
          deviceConnected();
        } else { // Setup device
          app.route = 'setup';
        }

      });
      app.route = 'home';
    }
    if (!backend.auth.getToken()) {
      app.route = 'login';
    }
  }

  function path(n, prop) {
    return 'valves.' + String(n) + '.' + prop;
  }

  function deviceConnected() {
    var request = app.waterApi.valve_info({
      device_id: app.device_id
    });
    request.execute(function(resp) {
      for (i = 0; i < 4; i++) {
        app.set(path(i, 'header'), resp.valves[i].name);
        var start_time = resp.valves[i].start_time;
        start_time = +start_time; // Make int
        if (start_time === 11 * 60 * 60) {
          app.set(path(i, 'startIndex'), 0);
        } else if (start_time === 14 * 60 * 60) {
          app.set(path(i, 'startIndex'), 1);
        } else if (start_time === 21 * 60 * 60 + 30 * 60) {
          app.set(path(i, 'startIndex'), 2);
        } else if (start_time === 23 * 60 * 60) {
          app.set(path(i, 'startIndex'), 3);
        }
        var duration_seconds = resp.valves[i].duration_seconds;
        app.set(path(i, 'hours'), Math.floor(duration_seconds / 3600));
        duration_seconds %= 3600;
        app.set(path(i, 'minutes'), Math.floor(duration_seconds / 60));
      }
      localStorage.valves = JSON.stringify(app.valves);
    });
  }

  app.useCurrentLocation = function() {
    app.geo = true;
    app.mapZoom = 13;
  };

  app.setupDone = function() {
    var request = app.waterApi.add_device({
      device_id: app.inputDeviceID,
      lat: app.lat,
      lng: app.lng
    });
    request.execute(function(resp) {
      if (resp.status === 'OK') { // Ok get data
        app.device_id = app.inputDeviceID;
        app.route = 'home';
        deviceConnected();
      } else { // Setup device
        // TODO add toast
        app.route = 'setup';
      }

    });
  };

  backend.addEventListener('google-api-load', function() {
    signin(true, userAuthed);
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
          color: '#F7464A',
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

  app.loginButtonPressed = function() {
    document.getElementById('loginButton').src = 'images/google_signin_pressed.svg';
    setTimeout(function() {
      document.getElementById('loginButton').src = 'images/google_signin.svg';
    }, 80);
    signin(false, userAuthed);
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
    if (typeof app.newPlants === 'undefined') {
      app.newPlants = [];
    }
    app.newPlants.forEach(function(z) {
      if (app.crops.indexOf(z.name) < 0) {
        var index = app.newPlants.indexOf(z);
        app.splice('newPlants', index);
      }
    });
    if (input) {
      e.target.options = app.cropsList.filter(function(item) {
        return item.toLowerCase().indexOf(input) !== -1;
      });
      e.target.options.sort(function(a, b) {
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
    } else {
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

    function update(){
      console.log('updt');
      var oldValves = JSON.parse(localStorage.valves);
      function sendUpdate(num) {
        var start = 0;
        if (app.valves[num].startIndex === 0) {
          start = 11 * 60 * 60;
        } else if (app.valves[num].startIndex === 1) {
          start = 14 * 60 * 60;
        } else if (app.valves[num].startIndex === 2) {
          start = 21 * 60 * 60 + 30 * 60;
        } else if (app.valves[num].startIndex === 3) {
          start = 23 * 60 * 60;
        }
        var duration = app.valves[num].hours * 3600 + app.valves[num].minutes * 60;
        var request = app.waterApi.valve_edit({
          device_id: app.device_id,
          number: num,
          duration_seconds: duration,
          start_time: start,
          name: app.valves[num].header
        });
        request.execute(function() {
          window.location.hash = '';
        });
      }

      for (i = 0; i < 4; i++) {
        if (JSON.stringify(app.valves[i]) === JSON.stringify(oldValves[i])) {
          window.location.hash = '';
        } else {
          sendUpdate(i);
        }
      }
    }

    var editors = document.getElementsByTagName('schedule-editor');
    for (var i = 0; i < editors.length; i++) {
      editors[i].addEventListener('update', update);
    }

  });

  // See https://github.com/Polymer/polymer/issues/1381
  window.addEventListener('WebComponentsReady', function() {
    // imports are loaded and elements have been registered
  });

  addEventListener('iron-select', function() {
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
