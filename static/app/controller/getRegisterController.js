


feasta.controller("RegisterController", [function ( $scope, $http){

    $scope.SendData = function () {
        // use $.param jQuery function to serialize data from JSON
        var data = $.param({
            first_name : $scope.first_name,
            last_name  : $scope.last_name,
            email      : $scope.email,
            phone_no   : $scope.phone_no,
            address    : $scope.address,
            location   : $scope.location,
            password1  : $scope.password1,
            password2  : $scope.password2
        });

        var config = {
            headers : {
                'Content-Type' : 'application/x-www-urlencoded;charset=utf-8;'
            }
        }

        $http.post("/api/v1/get-user/", data, config)
            .success(function (data, status, headers, config) {
                $scope.PostDataResponse = data;
            })

            .error(function (data, status, headers, config) {
                $scope.ResponseDetails = "DATA : " + data +
                "<hr />status : " + status  +
                "<hr />config : " + config;
            });
    };

}]);