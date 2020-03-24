var feasta = angular.module("feasta", ['ngRoute'])

feasta.constant('BASE_URL', "http://localhost:3000/api/v1/");


feasta.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);

    $routeProvider
        .when('/', {
            templateUrl: "static/app/app-template/index.html"
        })
        .when('/home/', {
            title: 'Home',
            templateUrl: "static/app/app-template/home.html",
            controller: "getMessController"
        })
        .when('/menu/', {
            templateUrl: "static/app/app-template/menu.html",
            controller: "getMenuController"
        })
        .when('/profile/',{
            templateUrl: "static/app/app-template/profile.html",
        })
        .when('/login/',{
            templateUrl: "static/app/app-template/login.html",
        })
    // .otherwise('/', {
    //     redirectTo: "/"
    // })

}]);

// feasta.run(['$rootScope', function ($rootScope) {
//     $rootScope.$on('$routeChangeSuccess', function (event, current, previous) {
//         $rootScope.title = current.$$route.title;
//     })

// }])
