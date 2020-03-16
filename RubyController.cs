using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RubyController : MonoBehaviour
{
    public int maxHealth = 5;
    public int Health { get { return currentHealth; } }
    int currentHealth;

    public float SPEED = 0.1f;
   

    Rigidbody2D rigidbody2D;
    // Start is called before the first frame update
    void Start()
    {
        
        rigidbody2D = GetComponent<Rigidbody2D>();
        currentHealth = maxHealth;
        Debug.Log(currentHealth + "/" + maxHealth);
        
    }

    // Update is called once per frame
    void Update()
    {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");
        //Debug.Log(horizontal);
        Vector2 position = rigidbody2D.position;
        position.x = position.x + SPEED * horizontal;
        position.y = position.y + 0.1f * vertical;
        rigidbody2D.MovePosition(position);
    }
    public void ChangeHealth(int amount)
    {
        currentHealth = Mathf.Clamp(currentHealth + amount, 0, maxHealth);
        Debug.Log(currentHealth + "/" + maxHealth);
    }
}
