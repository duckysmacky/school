SELECT d.article, d.author, d.knowledge_id
FROM Discoveries d
JOIN Epochs e ON d.epoch_id = e.id
JOIN Knowledge k ON d.knowledge_id = k.id
WHERE d.ecology < 0
    AND ((d.team < 10000 AND d.ants_dino = 0) OR (d.team < 5 AND d.ants_dino = 1))
    AND e.epoch IN ('Electric Era', 'Atomic Era', 'Information Era')
ORDER BY k.domain ASC, d.ecology ASC, d.author ASC;