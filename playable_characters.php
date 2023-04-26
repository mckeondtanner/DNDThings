<style>
    th, td {
        text-align: left;
        border-style: groove;
        border-color: #C0C0C0;
        font-family: "Times New Roman", Times, serif;
    }
</style>
    
    <?php
    
    $con=mysqli_connect("db.luddy.indiana.edu", "i308s23_mdtanner", "my+sql=i308s23_mdtanner", "i308s23_mdtanner");
    if (!$con) {die("Failed to connect to MySQL: " . mysqli_connect_error()); }
    
    $sql = "SELECT fname AS name, race, class, description FROM pc ORDER BY name ASC";
    
    $result = mysqli_query($con, $sql);
    $num_rows = mysqli_num_rows($result);
    if ($num_rows > 0) {
           echo "<table>";
           echo "<tr>
                           <th>PC Name</th>
                           <th>Race</th>
                           <th>Class</th>
                           <th>Description</th>
                      
                   </tr>";
           while($row = mysqli_fetch_assoc($result)) {
                   echo "<tr>
                  
                            <td>" . $row["name"]."</td>
                            <td>" . $row["race"]."</td>
                            <td>" . $row["class"]."</td>
                            <td>" . $row["description"]."</td>
                                 
                           </tr>";
           }
           echo "<table>";
    } else { echo "0 results"; }
    my_sql_close($conn);
    ?>