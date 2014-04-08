var partyApp = angular.module('partyApp', [
    'ngRoute',
    'partyControllers',
	'partyServices'
]);

partyApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/party-detail/:partyId', {
                templateUrl: '/templates/parties/party-detail.html',
                controller: 'PartyDetailCtrl'
            }).
            when('/party-overview/:partyId', {
                templateUrl: '/templates/parties/party-overview.html',
                controller: 'PartyOverviewCtrl'
            }).
            when('/message-detail/:messageId', {
                templateUrl: '/templates/parties/message-detail.html',
                controller: 'MessageDetailCtrl'
            }).
            when('/willingness-detail/:willingnessId', {
                templateUrl: '/templates/parties/willingness-detail.html',
                controller: 'WillingnessDetailCtrl'
            }).
            otherwise({
                templateUrl: '/templates/parties/index.html',
                controller: 'UserOverviewCtrl'
            });
    }
]);