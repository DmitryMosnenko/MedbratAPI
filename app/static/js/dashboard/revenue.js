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


app.controller('revenueController', ['$scope', '$rootScope', '$http', '$interval', '$filter',
    function($scope, $rootScope, $http, $interval, $filter) {
    $scope.summary = {};
    $scope.revenue = {value:"revenue", buttonStyle: "btn btn-info btn-row"};
    $scope.items = [];

    var fillItems = function() {
        $scope.items = [];
        $scope.summary.day = $rootScope.dateBegin === $rootScope.dateEnd ? $rootScope.dateBegin :
            $rootScope.dateBegin + "  -  " + $rootScope.dateEnd;

        var dB = new Date($rootScope.dateBegin);
        var dE = new Date($rootScope.dateEnd);
        for (d = dB; d <= dE; d.setDate(dB.getDate() + 1)) {
	    var date = $filter('date')(new Date(d),'yyyy-MM-dd');
            $scope.items[date] = {};
            $scope.items[date].date = date;
            $scope.items[date].revenue = {value:"revenue", buttonStyle: "btn btn-info btn-row"};
            $scope.items.push($scope.items[date]);
        }

        angular.forEach($scope.items, function(item) {
	    var date_range = item.date + "/" + item.date;
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
            $http.get("/checks/count/" + date_range)
                .success(function(response) {
                    item.checksNumber = parseFloat(response);
                });
            $http.get("/checks/avg/" + date_range)
                .success(function(response) {
                    item.avgCheck = parseFloat(response);
                });
        });
    }; fillItems();


    $scope.getRevenue = function(day) {
	dayNormalized = $filter('date')(day,'yyyy-MM-dd');
        date_range = dayNormalized + "/" + dayNormalized;
        $scope.items[day].revenue.value = "retrieving";
        $http.get("/revenue/" + date_range)
            .success(function(response) {
                $scope.items[day].revenue.value = parseFloat(response);
                $scope.items[day].revenue.buttonStyle = "btn btn-success btn-row";
            })
    };


    $scope.$on("date-range-changed", function(event, args) {
        fillItems();
    });
}]);
