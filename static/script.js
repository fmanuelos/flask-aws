(function(angular) {
  'use strict';
angular.module('myApp', [])
  .controller('ListController', ['$scope', '$http' ,function($scope, $http) {
    $http({
      method: 'GET',
      url: '/list'
    }).then(function successCallback(response) {
      $scope.data = response.data;
    }, function errorCallback(response) {
      console.log(response)
    });
  }])
})(window.angular);