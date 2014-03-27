var partyControllers = angular.module('weddingassist.party.controllers', ['ngAnimate', 'ngTouch']);

var partyServices = angular.module('weddingassist.party.services', ['ngResource']);
 
partyServices.factory('Party', ['$resource',
	function($resource){
		return $resource('phones/:phoneId.json', {}, {
			query: {method:'GET', params:{phoneId:'phones'}, isArray:true}
	});
}]);

partyControllers.controller('PartyDetailCtrl', ['$scope', '$http',
	function($scope, $http) {
		/*
		$http.get('party/' + $routeParams.partyId).success(function(data){
			$scope.title = data.title;
			$scope.subscription = data.subscription;
			$scope.date = data.date;
			$scope.time = data.time;
			$scope.location = data.location;
		});
		*/
		$scope.title = "Jerry & Yuchen's Wedding Banquet";
		$scope.subscription = "After a long run for eight years, we are decided to get married. All of my friends are welcome to my wedding party and banquet.";
		$scope.date = "2013-10-26";
		$scope.time = "16:30:00";
		$scope.location = "青青食尚花園會館";
		$scope.story = "我們兩個從來沒同班過，國中因緣際會和黃小真一起參加比賽，參加夏令營開始認識。至此開始通mail，開始傳簡訊，雖然沒有天天膩在一起，但也總是保持著聯絡。這樣的關係一直持續到高三前夕，大家一起在台北車站為聯考做最後的衝刺，至此我們的關係才開始變得親密。我們開始常常一起上課念書，一起翹課放鬆。三不五時就混再一起。大學分發結果出來後，我們很幸運的分發到了同一所學校。兩個即將要離鄉去遠地念書的人，開始走遍台北的各個角落，希望能多看看自己長大的這片土地。還記得前往台南前的兩個禮拜，我們幾乎天天都待在外面，晚上回家休息後，凌晨繼續出發。不管怎樣，就是享受最後的台北時光，怎樣都捨不得睡。進入大學後，兩個人在異鄉的人，做甚麼是總是第一個想到對方。";
		$scope.photo
		$scope.photos = [
			{src: 'userdata/img/photo1.jpg', desc: 'Image 1'},
			{src: 'userdata/img/photo2.jpg', desc: 'Image 2'},
			{src: 'userdata/img/photo3.jpg', desc: 'Image 3'},
			{src: 'userdata/img/photo4.jpg', desc: 'Image 4'},
			{src: 'userdata/img/photo5.jpg', desc: 'Image 5'},
			{src: 'userdata/img/photo6.jpg', desc: 'Image 6'},
			{src: 'userdata/img/photo7.jpg', desc: 'Image 7'},
			{src: 'userdata/img/photo8.jpg', desc: 'Image 8'},
			{src: 'userdata/img/photo9.jpg', desc: 'Image 9'},
			{src: 'userdata/img/photo10.jpg', desc: 'Image 10'},
			{src: 'userdata/img/photo11.jpg', desc: 'Image 11'},
			{src: 'userdata/img/photo12.jpg', desc: 'Image 12'},
			{src: 'userdata/img/photo13.jpg', desc: 'Image 13'}
		];
		$scope.messages = [
			{'author':'lien', 'datetime':'2013-11-12 08:08:08', 'body':'cowbey'},
			{'author':'lia', 'datetime':'2013-11-10 18:18:18', 'body':'babe'}	
		];

		// initial image index
		$scope._Index = 0;

		// if a current image is the same as requested image
		$scope.isActive = function (index) {
			return $scope._Index === index;
		};

		// show prev image
		$scope.showPrev = function () {
			$scope._Index = ($scope._Index > 0) ? --$scope._Index : $scope.photos.length - 1;
		};

		// show next image
		$scope.showNext = function () {
			$scope._Index = ($scope._Index < $scope.photos.length - 1) ? ++$scope._Index : 0;
		};

		// show a certain image
		$scope.showPhoto = function (index) {
			$scope._Index = index;
		};
	}
]);