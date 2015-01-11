var mainApp = angular.module('mainApp', ['ngRoute']);

mainApp.config(function($routeProvider) {
    $routeProvider

        // route for the home page
        .when('/', {
            templateUrl : '/static/html/index/main.html',
            controller  : 'mainController'
        })

        // route for the about page
        .when('/about', {
            templateUrl : '/static/html/index/about.html',
            controller  : 'aboutController'
        })

        // route for the contact page
        .when('/contact', {
            templateUrl : '/static/html/index/contact.html',
            controller  : 'contactController'
        });
});


function mainController($scope, $http, $interval) {
    $scope.summaryIncomes = 0;
    $scope.checksNumber = 0;
    $scope.avgCheck = 0;
    $scope.backgroundImage = {
        'background': 'url(/static/img/Facade.JPG)'
    };

    getAndFillScope = function() {
        var d = new Date();
        var curr_date = d.getDate();
        var curr_month = d.getMonth() + 1;
        var curr_year = d.getFullYear();

        date_range = curr_year + "-" + curr_month + "-01" + "/" + curr_year + "-" + curr_month + "-" + curr_date;
        $http.get("/incomes/" + date_range)
            .success(function (response) {
                $scope.summaryIncomes = parseFloat(response);
            });
        $http.get("/checks/count/" + date_range)
            .success(function(response) {
                $scope.checksNumber = response;
            });
        $http.get("/checks/avg/" + date_range)
            .success(function(response) {
                $scope.avgCheck = parseFloat(response);
            });
    }; getAndFillScope();

    var intervalPromise = $interval(getAndFillScope, 50000);
    $scope.$on('$destroy', function () { $interval.cancel(intervalPromise); });
}


function contactController($scope) {
    $scope.backgroundImage = {
        'background': 'url(/static/img/Showcase.JPG)',
        'background-position': 'center'
    }
}


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