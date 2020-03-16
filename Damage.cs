using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Damage : MonoBehaviour
{
    void OnTriggerStay2D(Collider2D other)
    {
        Debug.Log("В наш коллайдер зашел : " + other);

        RubyController controller = other.GetComponent<RubyController>();

        if (controller != null)
        {
           
            
          controller.ChangeHealth(-1);
                
          

        }
    }
}
