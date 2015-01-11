/**
 * Created by AMID on 1/11/15.
 */

var revenueApp = angular.module('dashboard.revenue', ['ngRoute']);

revenueApp.config(function($routeProvider) {
    $routeProvider

        // route for the revenue page
        .when('/revenue', {
            templateUrl : '/static/html/dashboard/revenue.html',
            controller  : 'revenueController'
        })
});


function revenueController($scope, $http, $interval) {
    $scope.summary = {};
    $scope.checks = {};
    $scope.revenue = {value:"revenue", buttonStyle: "btn btn-info"};

    getAndFillScope = function() {
        today =  getTodayDate();
        date_range = today + "/" + today;
        $scope.summary.day = today;

        $http.get("/incomes/" + date_range)
            .success(function(response) {
                $scope.summary.total_income = parseFloat(response);
            });
        $http.get("/checks/count/" + date_range)
            .success(function(response) {
                if ( $scope.summary.checks_number != parseFloat(response) ) {
                    $scope.summary.checks_number = parseFloat(response);
                    if (typeof $scope.revenue.value == 'number')
                        $scope.revenue.buttonStyle = "btn btn-warning";
                }
            });
        $http.get("/checks/summary/" + date_range)
            .success(function(response) {
                $scope.checks = merge_options(response, $scope.checks);
            });
    }; getAndFillScope();

    var intervalPromise = $interval(getAndFillScope, 50000);
    $scope.$on('$destroy', function () { $interval.cancel(intervalPromise); });

    $scope.getDetailsForCheck = function(id) {
        if (!$scope.checks[id].isVisible ||
            ($scope.checks[id].isVisible === false))
        {
            if (!$scope.checks[id].detail)
            {
                console.log("getDetailsForCheck: for ", id);
                $http.get("/checks/detail/" + id)
                    .success(function(response) {
                        console.log("===>", response)
                        $scope.checks[id].detail = response;
                        $scope.checks[id].isVisible = true
                    })
            }
            else
                $scope.checks[id].isVisible = true
        }
        else{
            $scope.checks[id].isVisible = false
        }
    };

    $scope.getRevenue = function() {
        today =  getTodayDate();
        date_range = today + "/" + today;
        $scope.revenue.value = "retrieving"
        $http.get("/revenue/" + date_range)
            .success(function(response) {
                $scope.revenue.value = parseFloat(response);
                $scope.revenue.buttonStyle = "btn btn-success";
            })
    }
}