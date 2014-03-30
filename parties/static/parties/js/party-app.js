var partyApp = angular.module('partyApp', [
    'ngRoute',
    'partyControllers'
]);

partyApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/party-detail/:partyId', {
                templateUrl: '/templates/parties/party-detail.html',
                controller: 'PartyDetailCtrl'
            }).
            when('/party-list', {
                templateUrl: '/templates/parties/party-list.html',
                controller: 'PartyListCtrl'
            }).
            otherwise({
                templateUrl: '/templates/parties/party-index.html',
                controller: 'PartyDetailCtrl'
            });
    }
]);