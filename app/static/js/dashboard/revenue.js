/**
 * Created by AMID on 1/11/15.
 */

var app = angular.module('dashboardApp');

app.config(function($routeProvider) {
    $routeProvider

        // route for the revenue page
        .when('/revenue', {
            templateUrl : '/static/html/dashboard/revenue.html',
            controller  : 'revenueController'
        })
});


app.controller('revenueController', ['$scope', '$rootScope', '$http', '$interval',
    function($scope, $rootScope, $http, $interval) {
    $scope.summary = {};
    $scope.checks = {};
    $scope.revenue = {value:"revenue", buttonStyle: "btn btn-info"};
    $scope.items = [];

    var fillItems = function() {
        $scope.items = [];
        $scope.summary.day = $rootScope.dateBegin === $rootScope.dateEnd ? $rootScope.dateBegin :
            $rootScope.dateBegin + "  -  " + $rootScope.dateEnd;

        var dB = new Date($rootScope.dateBegin);
        var dE = new Date($rootScope.dateEnd);
        for (d = dB; d <= dE; d.setDate(dB.getDate() + 1)) {
            $scope.items[d] = {};
            $scope.items[d].date = new Date(d);
            $scope.items[d].revenue = {value:"revenue", buttonStyle: "btn btn-info"};
            $scope.items.push($scope.items[d]);
        }

        angular.forEach($scope.items, function(item) {
            var date_range = new Date(item.date).toLocaleFormat('%Y-%m-%d') + "/"
                + new Date(item.date).toLocaleFormat('%Y-%m-%d');
            $http.get("/incomes/" + date_range)
                .success(function(response) {
                    item.totalDaySum = parseFloat(response);
                });
            $http.get("/incomes/cash/" + date_range)
                .success(function(response) {
                    item.cashDaySum = parseFloat(response);
                });
            $http.get("/incomes/terminal/" + date_range)
                .success(function(response) {
                    item.terminalDaySum = parseFloat(response);
                });
            $http.get("/incomes/rebate/" + date_range)
                .success(function(response) {
                    item.rebateDaySum = parseFloat(response);
                });
        });
    }; fillItems();


    $scope.getRevenue = function(day) {
        dayNormalized = day.toLocaleFormat('%Y-%m-%d');
        date_range = dayNormalized + "/" + dayNormalized;
        $scope.items[day].revenue.value = "retrieving";
        $http.get("/revenue/" + date_range)
            .success(function(response) {
                $scope.items[day].revenue.value = parseFloat(response);
                $scope.items[day].revenue.buttonStyle = "btn btn-success";
            })
    };


    $scope.$on("date-range-changed", function(event, args) {
        fillItems();
    });
}]);