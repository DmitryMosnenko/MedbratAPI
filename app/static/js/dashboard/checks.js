/**
 * Created by AMID on 1/11/15.
 */

var app = angular.module('dashboardApp');

app.config(function($routeProvider) {
    $routeProvider

        // route for the revenue page
        .when('/checks', {
            templateUrl : '/static/html/dashboard/checks.html',
            controller  : 'checksController'
        })
});


app.controller('checksController', ['$scope', '$rootScope', '$http', '$interval', '$filter',
    function($scope, $rootScope, $http, $interval, $filter) {
    $scope.summary = {};
    $scope.revenue = {value:"revenue", buttonStyle: "btn btn-info btn-row"};
    $scope.items = [];
    $scope.activeCheck = {};

    var fillItems = function() {
        $scope.items = [];
        $scope.summary.day = $rootScope.dateBegin === $rootScope.dateEnd ? $rootScope.dateBegin :
            $rootScope.dateBegin + "  -  " + $rootScope.dateEnd;

        var dB = new Date($rootScope.dateBegin);
        var dE = new Date($rootScope.dateEnd);
        for (d = dB; d <= dE; d.setDate(dB.getDate() + 1)) {
	    var date_range = $filter('date')(new Date(d),'yyyy-MM-dd') + "/"
		+ $filter('date')(new Date(d),'yyyy-MM-dd');
            $http.get("/checks/summary/" + date_range)
                .success(function (response) {
                    angular.forEach(response, function(responseItem) {
			responseItem.date = $filter('date')(d,'yyyy-MM-dd');
                        $scope.items.push(responseItem);
                    });
                });
        }
    }; fillItems();


    $scope.$on("date-range-changed", function(event, args) {
        fillItems();
    });


    $scope.getDetailsForCheck = function(check) {
        if (!check.detail) {
            $http.get("/checks/detail/" + check.id)
                .success(function(response) {
                    check.detail = response;
                    $scope.activeCheck = check;
                })
        }
        else
            $scope.activeCheck = check;

        if ($scope.lastSelected) {
            $scope.lastSelected.isActive = '';
        }
        this.isActive = 'selected';
        $scope.lastSelected = this;
    };
}]);
