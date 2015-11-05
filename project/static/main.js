var app = angular.module('webtasks', ['ngResource']);

app.factory("Task", function($resource) {
  return $resource(
    "/task/:id"
    ,
    {},
    {
        get_objects: { method: "GET", isArray: false },
    }
  );
});

app.controller('WebTasksController', function($scope, Task) {

    Task.get_objects(
        function(data) {
            $scope.tasks = data.objects;
        }
    );

    $scope.add_task = function() {
        var task = new Task();
        task.task = $scope.new_task.trim();
        Task.save(task);

        // This will update the GUI... must have a better way of doing that!
        Task.get_objects(
            function(data) {
                $scope.tasks = data.objects;
            }
        );

        $scope.new_task = '';
    }

    $scope.delete_all = function() {
        Task.remove();

        // This will update the GUI... must have a better way of doing that!
        Task.get_objects(
            function(data) {
                $scope.tasks = data.objects;
            }
        );
    }

    $scope.delete_task = function(id) {
        console.log('delete ' + id);

        Task.remove({id: id});

        // This will update the GUI... must have a better way of doing that!
        Task.get_objects(
            function(data) {
                $scope.tasks = data.objects;
            }
        );
    }


    $scope.toogle_task = function(id) {
        console.log('toogle ' + id);
    }


    $scope.edit_task = function(id) {
        console.log('edit ' + id);
    }

});

