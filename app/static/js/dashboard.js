/**
 * Created by AMID on 1/11/15.
 */

var dashboardApp = angular.module('dashboardApp', ['ngRoute']);

dashboardApp.run(function($rootScope) {
    $rootScope.dateBegin = $rootScope.dateEnd = getTodayDate();
});

dashboardApp.controller('todayController', ['$rootScope',
    function($rootScope) {
        $rootScope.dateBegin = getTodayDate();
        $rootScope.dateEnd = getTodayDate();
}]);


function getTodayDate() {
    var d = new Date();
    var curr_date = d.getDate();
    var curr_month = d.getMonth() + 1;
    var curr_year = d.getFullYear();

    today =  curr_year + "-" + curr_month + "-" + curr_date;
    return today;
}