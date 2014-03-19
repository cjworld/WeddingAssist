var noterControllers = angular.module('noterControllers', []);

noterControllers.controller('MemoListCtrl', ['$scope', 'MemoList', function($scope, MemoList) {
    $scope.memos = MemoList.query();
}]);

noterControllers.controller('NotebookListCtrl', ['$scope', 'NotebookList', function($scope, NotebookList) {
        $scope.notebooks = NotebookList.query();
}]);