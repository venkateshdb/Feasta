/*
feasta Mess controller, use to display
all mess
*/

feasta.controller('getMessController', ['$scope', '$http', function ($scope, $http) {
    $scope.Mess = {};

    $http.get("/api/v1/get-mess/", )
        .success(function (data) {
            $scope.Mess = data;
            console.log(data);
        })
        .error(function (data, status, value) {
            console.log("error occured");
        })
}]);
