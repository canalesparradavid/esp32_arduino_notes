<?php
// Nombre de la base de datos SQLite
$databaseFile = 'logs.db';

try {
    // Conexión a la base de datos
    $db = new PDO('sqlite:' . $databaseFile);

    // Consulta SQL para seleccionar todos los registros de la tabla 'logs'
    $query = 'SELECT * FROM logs';

    // Ejecutar la consulta
    $stmt = $db->query($query);

    // Obtener todos los registros como un array asociativo
    $logs = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Cerrar la conexión a la base de datos
    $db = null;

    // Devolver los registros en formato JSON
    header('Content-Type: application/json');
    echo json_encode($logs);
} catch (PDOException $e) {
    header('Content-Type: application/json');
    echo json_encode("");
}
?>
