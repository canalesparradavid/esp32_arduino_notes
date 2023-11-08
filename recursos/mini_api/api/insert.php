<?php
// Nombre de la base de datos SQLite
$databaseFile = 'logs.db';

if (isset($_GET['fecha']) && isset($_GET['descripcion'])) {
    // Procesar los datos de la solicitud GET
    $fecha = $_GET['fecha'];
    $descripcion = $_GET['descripcion'];

    try {
        // Conexión a la base de datos
        $db = new PDO('sqlite:' . $databaseFile);

        // Consulta SQL para insertar un nuevo registro en la tabla 'logs'
        $query = 'INSERT INTO logs (fecha, descripcion) VALUES (:fecha, :descripcion)';

        // Preparar la consulta
        $stmt = $db->prepare($query);

        // Bind de los parámetros
        $stmt->bindParam(':fecha', $fecha);
        $stmt->bindParam(':descripcion', $descripcion);

        // Ejecutar la consulta
        $stmt->execute();

        // Cerrar la conexión a la base de datos
        $db = null;
    } catch (PDOException $e) { }
}

header('Content-Type: application/json');
echo json_encode([]);
?>
