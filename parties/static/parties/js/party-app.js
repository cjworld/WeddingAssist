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
            when('/userparty-list', {
                templateUrl: '/templates/parties/userparty-list.html',
                controller: 'UserPartyListCtrl'
            }).
            when('/party-detail/:partyId', {
                templateUrl: '/templates/parties/party-detail.html',
                controller: 'PartyDetailCtrl'
            }).
            when('/usermessage-list', {
                templateUrl: '/templates/parties/usermessage-list.html',
                controller: 'UserMessageListCtrl'
            }).
            when('/message-detail/:messageId', {
                templateUrl: '/templates/parties/message-detail.html',
                controller: 'MessageDetailCtrl'
            }).
            when('/userwillingness-list', {
                templateUrl: '/templates/parties/userwillingness-list.html',
                controller: 'UserWillingnessListCtrl'
            }).
            when('/willingness-detail/:willingnessId', {
                templateUrl: '/templates/parties/willingness-detail.html',
                controller: 'WillingnessDetailCtrl'
            }).
            otherwise({
                templateUrl: '/templates/parties/index.html',
                controller: 'PartyDetailCtrl'
            });
    }
]);