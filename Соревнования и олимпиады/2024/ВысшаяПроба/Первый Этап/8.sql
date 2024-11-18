SELECT *
FROM "Discoveries" d
JOIN "Epochs" e ON d.epoch_id = e.id
JOIN "Knowledge" k ON d.knowledge_id = k.id
WHERE ((d.team > 10000 AND d.ants_dino = 0) OR (d.team > 5 AND d.ants_dino = 1))
    AND e.epoch in ('Electric Era', 'Information Era')