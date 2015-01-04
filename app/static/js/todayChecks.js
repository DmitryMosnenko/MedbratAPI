function todayChecksController($scope, $http, $interval) {
    $scope.summary = {};
    $scope.checks = {};

    getAndFillScope = function() {
        var d = new Date();
        var curr_date = d.getDate();
        var curr_month = d.getMonth() + 1;
        var curr_year = d.getFullYear();

        today =  curr_year + "-" + curr_month + "-" + curr_date;
        date_range = today + "/" + today;
        $scope.summary.day = today;

        $http.get("/incomes/" + date_range)
            .success(function(response) {
                $scope.summary.total_income = parseFloat(response);
            });
        $http.get("/checks/count/" + date_range)
            .success(function(response) {
                $scope.summary.checks_number = parseFloat(response);
            });
        $http.get("/checks/summary/" + date_range)
            .success(function(response) {
                $scope.checks = merge_options(response, $scope.checks);
            });
    }; getAndFillScope();

    var intervalPromise = $interval(getAndFillScope, 5000);
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