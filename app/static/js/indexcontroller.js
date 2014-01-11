'use strict';

var app = angular.module('rsswala',['ngRoute']);

function itemsCtrl($scope, $http) {

  $scope.items = [];

  $scope.getFeeds = function () {

      $http({

        method:'GET',
        url:'/feeds/items'

      }).success(
          function(data, status, headers, config) {
            $scope.items = data;
          })
        .error(
          function(data, status, headers, config) {
            console.log("error",data);
          });

  };

  $scope.getFeeds();
}
