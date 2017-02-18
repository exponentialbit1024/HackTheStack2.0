var app = angular.module('hackTStack', ['ngMaterial'])
  .config(function($mdThemingProvider){
    $mdThemingProvider.theme('default')
      .primaryPalette('blue')
      .backgroundPalette('grey')
      .accentPalette('blue-grey')
      .warnPalette('red');
  });

app.controller("indexCtrl", function($scope, $http, $window){

  $scope.pid = {};

  $scope.submitLID = function(){
    if($scope.pid != null){
      $http({
        method  : 'POST',
        url     : '/loginAuth',
        data    : $scope.pid,
        headers : {'Content-Type': 'application/json'}
       })
       .success(function(data) {
         console.log(data);
          if (data.errors) {
            // Showing errors.
            $scope.errorName = data.errors.name;
            $scope.errorUserName = data.errors.username;
            $scope.errorEmail = data.errors.email;
          } else {
            $scope.message = data.message;
            if(data.result){
              $window.location.href = '/';
            }else{
              alert("Crash and burn, call a moderator");
            }
          }
        });
      }
  };
});

app.controller("challengeCtrl", function($scope, $http, $window){
  $scope.boa1submitflag =  false;
  $scope.boa2submitflag =  false;
  $scope.boa3submitflag =  false;
  $scope.boa4submitflag =  false;
  $scope.boa5submitflag =  false;

  $scope.boa = {};
  $scope.buttonToggle = [];
  checkDBaseBOA();
  function checkDBaseBOA(){
    $http.get('/getBOADBase')
    .then(function(response){
      console.log(response);
      $scope.buttonToggle = response.data.allChallenges;
      while($scope.buttonToggle.length != 5){
        $scope.buttonToggle.push(false);
      }
      $scope.boa1submitflag =  $scope.buttonToggle[0];
      $scope.boa2submitflag =  $scope.buttonToggle[1];
      $scope.boa3submitflag =  $scope.buttonToggle[2];
      $scope.boa4submitflag =  $scope.buttonToggle[3];
      $scope.boa5submitflag =  $scope.buttonToggle[4];
    });
  }

  $scope.boa1passSubmit = function(){
    var tempboa1 = $scope.boapass1;
    var tempboa2 = $scope.boapass2;
    var tempboa3 = $scope.boapass3;
    var tempboa4 = $scope.boapass4;
    var tempboa5 = $scope.boapass5;

    if($scope.boapass1 == null){
      tempboa1 = "";
    }
    if($scope.boapass2 == null){
      tempboa2 = "";
    }
    if($scope.boapass3 == null){
      tempboa3 = "";
    }
    if($scope.boapass4 == null){
      tempboa4 = "";
    }
    if($scope.boapass5 == null){
      tempboa5 = "";
    }

    var boaPass = {
      'boa1' : tempboa1,
      'boa2' : tempboa2,
      'boa3' : tempboa3,
      'boa4' : tempboa4,
      'boa5' : tempboa5
    };
    $http({
      method  : 'POST',
      url     : '/checkBOA',
      data    : boaPass,
      headers : {'Content-Type': 'application/json'}
     })
     .success(function(data) {
        if (data.errors) {
          // Showing errors.
          $scope.errorName = data.errors.name;
          $scope.errorUserName = data.errors.username;
          $scope.errorEmail = data.errors.email;
        } else {
          $scope.message = data.message;
          if(data.result){
            //check for database for button toggle
            checkDBaseBOA();
          }else{
            alert("Crash and burn, call a moderator");
          }
        }
      });
  };

})
