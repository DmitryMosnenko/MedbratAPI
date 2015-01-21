/**
 * Created by AMID on 1/11/15.
 */

var dashboardApp = angular.module('dashboardApp', ['ngRoute']);

dashboardApp.run(function($rootScope) {
    $rootScope.dateBegin = $rootScope.dateEnd = new Date().toLocaleFormat('%Y-%m-%d');
});


dashboardApp.controller('globalMenuController', ['$rootScope', '$scope',
    function($rootScope, $scope) {
        $scope.dateRangeUpdated = function() {
            $rootScope.dateBegin = $scope.dateBegin;
            $rootScope.dateEnd = $scope.dateEnd;
            $rootScope.$broadcast('date-range-changed');
        };
}]);

dashboardApp.controller('globalMenuSwitcherController', ['$scope', '$location',
    function($scope, $location) {
        $scope.menuItems = [/*{
                              EndPoint  : 'home',
                              Text      : 'Home'
                            },*/ {
                              EndPoint  : 'revenue',
                              Text      : 'Revenue'
                            }, {
                              EndPoint  : 'checks',
                              Text      : 'Checks'
                            }];

        $scope.isMenuItemActive = function (page) {
            var currentRoute = $location.path().substring(1) || 'home';
            return page === currentRoute ? 'active' : '';
        };
}]);