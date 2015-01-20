var app = angular.module('dashboardApp');

app.config(function($routeProvider) {
    $routeProvider

        // route for the revenue page
        .when('/', {
            templateUrl : '/static/html/dashboard/today.html',
            controller  : 'todayController'
        })
});


app.controller('todayController', ['$scope', '$rootScope', '$http', '$interval',
    function($scope, $rootScope, $http, $interval) {
    $scope.summary = {};
    $scope.checks = {};
    $scope.revenue = {value:"revenue", buttonStyle: "btn btn-lg btn-info btn-block"};

    getAndFillScope = function() {
        date_range = $rootScope.dateBegin + "/" + $rootScope.dateEnd;
        $scope.summary.day = $rootScope.dateBegin === $rootScope.dateEnd ? $rootScope.dateBegin :
            $rootScope.dateBegin + "  -  " + $rootScope.dateEnd;

        $http.get("/incomes/" + date_range)
            .success(function(response) {
                $scope.summary.total_income = parseFloat(response);
            });
        $http.get("/checks/count/" + date_range)
            .success(function(response) {
                if ( $scope.summary.checks_number != parseFloat(response) ) {
                    $scope.summary.checks_number = parseFloat(response);
                    if (typeof $scope.revenue.value == 'number')
                        $scope.revenue.buttonStyle = "btn btn-lg btn-warning btn-block";
                }
            });
    }; getAndFillScope();

    $scope.$on("date-range-changed", function(event, args) {
        getAndFillScope();
    });

    var intervalPromise = $interval(getAndFillScope, 50000);
    $scope.$on('$destroy', function () { $interval.cancel(intervalPromise); });

    $scope.getRevenue = function() {
        date_range = $rootScope.dateBegin + "/" + $rootScope.dateEnd;
        $scope.revenue.value = "retrieving"
        $http.get("/revenue/" + date_range)
            .success(function(response) {
                $scope.revenue.value = parseFloat(response);
                $scope.revenue.buttonStyle = "btn btn-lg btn-success btn-block";
            })
    }
}]);

/**
 * Overwrites obj1's values with obj2's and adds obj2's if non existent in obj1
 * @param obj1
 * @param obj2
 * @returns obj3 a new object based on obj1 and obj2
 */
function merge_options(obj1,obj2){
    var obj3 = {};
    for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
    for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
    return obj3;
}