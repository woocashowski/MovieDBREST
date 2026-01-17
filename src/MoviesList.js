import {useState} from "react";
import MovieForm from "./MovieForm";

export default function MoviesList({movies}) {
   return (
        <div>
           <h1>Lista moich ulubionych filmów:</h1>
           <ul>
               {movies.map(movie =>
                   <li key={movie.title}>{movie.title} ({movie.year})</li>
               )}
           </ul>
        </div>
   );
}
