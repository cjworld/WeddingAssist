var noterServices = angular.module('noterServices', ['ngResource']);

noterServices.factory('Memo', ['$resource',
    function($resource) {
        return $resource('memos/:id');
    }
]);

noterServices.factory('MemoList', ['$resource',
    function($resource) {
        return $resource('memos/');
    }
]);

noterServices.factory('Notebook', ['$resource',
    function($resource) {
        return $resource('notebooks/:id');
    }
]);

noterServices.factory('NotebookList', ['$resource',
    function($resource) {
        return $resource('notebooks/');
    }
]);