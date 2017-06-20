/*
Copyright (c) 2015 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/
/* jshint -W106 */
//jscs:disable maximumLineLength
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

function mod(n, m) {
  return ((n % m) + m) % m;
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
  var i;

  function path(n, prop) {
    return 'valves.' + String(n) + '.' + prop;
  }

  app.valveNameList = [
    {'name': 'Valve 1', 'url': ''},
    {'name': 'Valve 2', 'url': ''},
    {'name': 'Valve 3', 'url': ''},
    {'name': 'Valve 4', 'url': ''},
    {
      'name': 'Vegetable Garden',
      'url': 'https://upload.wikimedia.org/wikipedia/commons/a/a2/Jardin_potager_6.jpg'
    },
    {
      'name': 'English Garden',
      'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Knot_Garden_at_Little_Moreton_Hall%2C_Cheshire_-_geograph.org.uk_-_1527.jpg'
    },
    {
      'name': 'Oranges',
      'url': 'https://upload.wikimedia.org/wikipedia/commons/b/b0/OrangeBloss_wb.jpg'
    },
    {
      'name': 'Lawn',
      'url': 'https://upload.wikimedia.org/wikipedia/commons/2/2f/%28Unmowed%29_grass_4.JPG'
    },
  ];

  function updateDonutChart() {
    var timeAllValves = app.valves[0].total_seconds + app.valves[1].total_seconds + app.valves[2].total_seconds + app.valves[3].total_seconds;
    function createPrecentage(i) {
      return Math.round(app.valves[i].total_seconds / timeAllValves * 100);
    }
    if (timeAllValves > 0) {
      app.usageRelativeData = [
            {
              value: createPrecentage(0),
              color: '#2196F3',
              highlight: '#1565C0',
              label: app.valves[0].header
            },
            {
              value: createPrecentage(1),
              color: '#FF9800',
              highlight: '#EF6C00',
              label: app.valves[1].header
            },
            {
              value: createPrecentage(2),
              color: '#E91E63',
              highlight: '#AD1457',
              label: app.valves[2].header
            },
            {
              value: createPrecentage(3),
              color: '#4CAF50',
              highlight: '#2E7D32',
              label: app.valves[3].header
            }
      ];
    } else {
      app.usageRelativeData = [
            {
              value: 100,
              color: '#BDBDBD',
              highlight: '#BDBDBD',
              label: 'No Data'
            }
      ];
    }
  }

  function updateLineChart(data) {
    if (data) {
      for (i = 0; i < data.length; i++) {
        data[i] = Math.round(data[i] * 100);
      }
      for (i = 0; data.length < 7; i++) {
        data.unshift(null);
      }
    }
    console.log(data);
    var d = new Date();
    var dow = d.getDay();
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var adjusted = [];
    for (i = 6; i >= 0; i--) {
      adjusted.push(days[mod((dow - i), 7)]);
    }
    app.usageTimeData = {
      labels: adjusted,
      datasets: [
        {
          label: 'My First dataset',
          fillColor: 'rgba(33, 150, 243, 0.2)',
          strokeColor: '#2196F3',
          pointColor: '#1976D2',
          pointStrokeColor: '#fff',
          pointHighlightFill: '#fff',
          pointHighlightStroke: 'rgba(220,220,220,1)',
          data: [59, 45, 61, 32, 41, 76, 32]
        }

      ]
    };
  }

  var a;

  var filterMethod = function(obj) {
    return obj.name.indexOf(a) > -1;
  };

  function setImg(i) {
    a = app.valves[i].header;
    var result = app.valveNameList.filter(filterMethod);
    if (0 < result.length) {
      app.set(path(i, 'image'), result[0].url);
    } else {
      a = app.valves[i].header.replace(/\s+/g, ',').toLowerCase();
      app.set(path(i, 'image'), 'https://source.unsplash.com/400x200/weekly?' + a);
    }
  }

  i = 0;
  if (!localStorage.valves) {
    app.valves = {};
    for (i = 0; i < 4; i++) {
      app.valves[i] = {};
      app.valves[i].header = 'Valve ' + String(i + 1);
      app.valves[i].startIndex = 1;
      app.valves[i].hours = 0;
      app.valves[i].minutes = 0;
      app.valves[i].total_seconds = 0;
      app.valves[i].url = 'valve' + String(i + 1);
    }
    localStorage.valves = JSON.stringify(app.valves);
  } else {
    app.valves = JSON.parse(localStorage.valves);
    updateDonutChart();
  }

  var backend = document.getElementById('backend');
  var CLIENT_ID = '651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com';
  var SCOPES = ['email', 'profile'];

  function signin(mode, authorizeCallback) {
    backend.auth.authorize({client_id: CLIENT_ID,
      scope: SCOPES, immediate: mode},
      authorizeCallback);
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
        app.set(path(i, 'total_seconds'), +duration_seconds);
        app.set(path(i, 'hours'), Math.floor(duration_seconds / 3600));
        duration_seconds %= 3600;
        app.set(path(i, 'minutes'), Math.floor(duration_seconds / 60));

        setImg(i);
        updateDonutChart();
      }
      localStorage.valves = JSON.stringify(app.valves);
    });

    request = app.waterApi.get_usage({
      device_id: app.device_id,
      datapoint_num: 7,
      datapoint_freq: 'DAY',
    });
    request.execute(function(resp) {
      updateLineChart(resp.usage);
      localStorage.valves = JSON.stringify(app.valves);
    });
  }

  function userAuthed() {
    var oldLocation = app.route;
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
          app.$.paperDrawerPanel.forceNarrow = true;
          //app.route = 'setup';
          app.setupDone();
        }

      });
      console.log(app.route);
      if (app.route === 'setup' || app.route === 'login') {
        //app.route = 'home';
        app.$.paperDrawerPanel.forceNarrow = false;
        page('/app');
      } else {
        app.route = oldLocation;
      }

    }
    if (!backend.auth.getToken()) {
      app.route = 'login';
    }
  }

  app.useCurrentLocation = function() {
    app.geo = true;
    app.mapZoom = 13;
  };

  app.setupDone = function() {
    var request = app.waterApi.add_device({
      device_id: Math.floor(Math.random() * 1000000).toString(),
      lat: 37.7,
      lng: -122.45
    });
    request.execute(function(resp) {
      if (resp.status === 'OK') { // Ok get data
        app.device_id = app.inputDeviceID;
        app.route = 'home';
        app.$.paperDrawerPanel.forceNarrow = false;
        deviceConnected();
      } else { // Setup device
        // TODO add toast
        app.$.paperDrawerPanel.forceNarrow = true;
        //app.route = 'setup';
      }

    });
  };

  backend.addEventListener('google-api-load', function() {
    signin(true, userAuthed);
  });

  app.chartOptions = {
    scaleOverride: true,
    scaleSteps: 4,
    scaleStepWidth: 25,
    scaleStartValue: 0,
    animation: false,
    scaleFontSize: 14,
    responsive: false,
    tooltipTemplate: '<%if (label){%><%=label%>: <%}%><%= value %>%',
  };

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
    for (i = 0; i < 4; i++) {
      //setImg(i);
    }
    function update() {
      var oldValves = JSON.parse(localStorage.valves);
      function sendUpdate(num) {
        console.log('update');
        var start = 0;
        if (app.valves[num].startIndex === 0) {
          start = 3 * 60 * 60;
        } else if (app.valves[num].startIndex === 1) {
          start = 6 * 60 * 60;
        } else if (app.valves[num].startIndex === 2) {
          start = 13 * 60 * 60 + 30 * 60;
        } else if (app.valves[num].startIndex === 3) {
          start = 15 * 60 * 60;
        }
        var duration = app.valves[num].hours * 3600 + app.valves[num].minutes * 60;
        app.set(path(num, 'total_seconds'), duration);
        updateDonutChart();
        var request = app.waterApi.valve_edit({
          device_id: app.device_id,
          number: num,
          duration_seconds: duration,
          start_time: start,
          name: app.valves[num].header
        });
        request.execute(function() {
          page('/app');
          app.$.toast.text = 'Schedule Updated';
          app.$.toast.show();
        });
      }

      for (var i = 0; i < 4; i++) {
        if (JSON.stringify(app.valves[i]) === JSON.stringify(oldValves[i])) {
          page('/app');
        } else {
          sendUpdate(i);
        }
      }
    }

    var editors = document.getElementsByTagName('schedule-editor');
    for (i = 0; i < editors.length; i++) {
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
    var detail = e.detail;
    var heightDiff = detail.height - detail.condensedHeight;
    var yRatio = Math.min(1, detail.y / heightDiff);
    // appName max size when condensed. The smaller the number the smaller the condensed size.
    var maxMiddleScale = 0.75;
    var auxHeight = heightDiff - detail.y;
    var auxScale = heightDiff / (1 - maxMiddleScale);
    var scaleMiddle = Math.max(maxMiddleScale, auxHeight / auxScale + maxMiddleScale);

    // Move/translate middleContainer
    Polymer.Base.transform('translate3d(0,' + yRatio * 100 + '%,0)', middleContainer);

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
