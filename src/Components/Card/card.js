import React from 'react';

export const Card = ({ listOfTodos })=> {
    return (
        <ul>
            { listOfTodos.map(todo => {
                return(
                <li key={todo.id}>
                    {todo.content}
                </li>
                )
            })}
        </ul>
    )
}