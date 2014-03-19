var notersApp = angular.module('notersApp.resource', [MemoServices]);

notersApp.controller('MemoCtrl', ['$scope', '$Memo', function($scope, $Memo) {
    $scope.memos = Memo.query();
}]);