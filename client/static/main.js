var app = angular.module('webtasks', ['ngResource']);

app.factory("Task", function($resource) {
  return $resource(
    "http://localhost:5000/task/:id"
    ,
    {},
    {
        query: { method: "GET", isArray: false },
        patch: { method: "PATCH" }
    }
  );
});

app.controller('WebTasksController', function($scope, Task) {

    Task.query(
        function(data) {
            $scope.tasks = data.objects;
        }
    );

    $scope.add_task = function() {
        var task = new Task();
        task.task = $scope.new_task.trim();
        task.done = true;
        task.$save(
            function(_ignore) {
                // Updates the list of objects. There must be a better way.
                Task.query(
                    function(data) {
                        $scope.tasks = data.objects;
                    }
                );
            }
        );
        $scope.new_task = '';
    }

    $scope.delete_all = function() {
        Task.remove(
            function(_ignore) {Task.query(function(data) {$scope.tasks = data.objects;});}
        );
    }

    $scope.delete_task = function(task) {
        Task.remove(
            {id: task.id},
            function(_ignore) {Task.query(function(data) {$scope.tasks = data.objects;});}
        );
    }

    $scope.toggle_task = function(task) {
        Task.get(
            {id:task.id},
            function(t, http_header) {
                t.done = task.done;
                t.$patch({id: t.id})
            }
        )
    }
});

