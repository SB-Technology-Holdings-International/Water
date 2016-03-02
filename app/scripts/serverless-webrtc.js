/* See also:
    http://www.html5rocks.com/en/tutorials/webrtc/basics/
    https://code.google.com/p/webrtc-samples/source/browse/trunk/apprtc/index.html

    https://webrtc-demos.appspot.com/html/pc1.html
*/
var cfg = { 'iceServers': [{ 'url': 'stun:23.21.150.121' }] }, con = { 'optional': [{ 'DtlsSrtpKeyAgreement': true }] };
/* THIS IS ALICE, THE CALLER/SENDER */
var pc1 = new RTCPeerConnection(cfg, con), dc1 = null, tn1 = null;
// Since the same JS file contains code for both sides of the connection,
// activedc tracks which of the two possible datachannel variables we're using.
var activedc;
var pc1icedone = false;
offerReceived = function (offer) {
  var offerDesc = new RTCSessionDescription(JSON.parse(offer));
  console.log('Received remote offer', offerDesc);
  handleOfferFromPC1(offerDesc);
};
answerReceived = function (answer) {
  var answerDesc = new RTCSessionDescription(JSON.parse(answer));
  handleAnswerFromPC2(answerDesc);
};
function fileSent(file) {
  console.log(file + ' sent');
}
function fileProgress(file) {
  console.log(file + ' progress');
}
function sendFile(data) {
  if (data.size) {
    FileSender.send({
      file: data,
      onFileSent: fileSent,
      onFileProgress: fileProgress
    });
  }
}
function sendMessage(msg) {
  var channel = new RTCMultiSession();
  channel.send({ message: msg });
  console.log('sent: ' + msg);
}
function setupDC1() {
  try {
    var fileReceiver1 = new FileReceiver();
    dc1 = pc1.createDataChannel('test', { reliable: true });
    activedc = dc1;
    console.log('Created datachannel (pc1)');
    dc1.onopen = function (e) {
      console.log('data channel connect');
    };
    dc1.onmessage = function (e) {
      console.log('Got message (pc1)', e.data);
      if (e.data.size) {
        fileReceiver1.receive(e.data, {});
      } else {
        if (e.data.charCodeAt(0) === 2) {
          // The first message we get from Firefox (but not Chrome)
          // is literal ASCII 2 and I don't understand why -- if we
          // leave it in, JSON.parse() will barf.
          return;
        }
        console.log(e);
        var data = JSON.parse(e.data);
        if (data.type === 'file') {
          fileReceiver1.receive(e.data, {});
        } else {
          console.log('received: ' + data.message);
        }
      }
    };
  } catch (e) {
    console.warn('No data channel (pc1)', e);
  }
}
function createLocalOffer() {
  setupDC1();
  pc1.createOffer(function (desc) {
    pc1.setLocalDescription(desc, function () {
    }, function () {
    });
    console.log('created local offer', desc);
  }, function () {
    console.warn('Couldn\'t create offer');
  });
}
pc1.onicecandidate = function (e) {
  console.log('ICE candidate (pc1)', e);
  if (e.candidate === null) {
    console.log(JSON.stringify(pc1.localDescription));
  }
};
function handleOnconnection() {
  console.log('Datachannel connected');
}
pc1.onconnection = handleOnconnection;
function onsignalingstatechange(state) {
  console.info('signaling state change:', state);
}
function oniceconnectionstatechange(state) {
  console.info('ice connection state change:', state);
}
function onicegatheringstatechange(state) {
  console.info('ice gathering state change:', state);
}
pc1.onsignalingstatechange = onsignalingstatechange;
pc1.oniceconnectionstatechange = oniceconnectionstatechange;
pc1.onicegatheringstatechange = onicegatheringstatechange;
function handleAnswerFromPC2(answerDesc) {
  console.log('Received remote answer: ', answerDesc);
  pc1.setRemoteDescription(answerDesc);
}
function handleCandidateFromPC2(iceCandidate) {
  pc1.addIceCandidate(iceCandidate);
}
/* THIS IS BOB, THE ANSWERER/RECEIVER */
var pc2 = new RTCPeerConnection(cfg, con), dc2 = null;
var pc2icedone = false;
pc2.ondatachannel = function (e) {
  var fileReceiver2 = new FileReceiver();
  var datachannel = e.channel || e;
  // Chrome sends event, FF sends raw channel
  console.log('Received datachannel (pc2)', arguments);
  dc2 = datachannel;
  activedc = dc2;
  dc2.onopen = function (e) {
    console.log('data channel connect');
  };
  dc2.onmessage = function (e) {
    console.log('Got message (pc2)', e.data);
    if (e.data.size) {
      fileReceiver2.receive(e.data, {});
    } else {
      var data = JSON.parse(e.data);
      if (data.type === 'file') {
        fileReceiver2.receive(e.data, {});
      } else {
        console.log('received: ' + data.message);
      }
    }
  };
};
function handleOfferFromPC1(offerDesc) {
  pc2.setRemoteDescription(offerDesc);
  pc2.createAnswer(function (answerDesc) {
    console.log('Created local answer: ', answerDesc);
    pc2.setLocalDescription(answerDesc);
  }, function () {
    console.warn('No create answer');
  });
}
pc2.onicecandidate = function (e) {
  console.log('ICE candidate (pc2)', e);
  if (e.candidate === null) {
      console.log(JSON.stringify(pc2.localDescription));
  }
};
pc2.onsignalingstatechange = onsignalingstatechange;
pc2.oniceconnectionstatechange = oniceconnectionstatechange;
pc2.onicegatheringstatechange = onicegatheringstatechange;
function handleCandidateFromPC1(iceCandidate) {
  pc2.addIceCandidate(iceCandidate);
}
pc2.onaddstream = function (e) {
  console.log('Got remote stream', e);
  var el = new Audio();
  el.autoplay = true;
  attachMediaStream(el, e.stream);
};
pc2.onconnection = handleOnconnection;
function getTimestamp() {
  var totalSec = new Date().getTime() / 1000;
  var hours = parseInt(totalSec / 3600) % 24;
  var minutes = parseInt(totalSec / 60) % 60;
  var seconds = parseInt(totalSec % 60);
  var result = (hours < 10 ? '0' + hours : hours) + ':' + (minutes < 10 ? '0' + minutes : minutes) + ':' + (seconds < 10 ? '0' + seconds : seconds);
  return result;
}
